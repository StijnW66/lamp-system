package com.lampsystem.lampsystem.Controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.beans.factory.annotation.Autowired;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;



import com.lampsystem.lampsystem.Entities.*;
import com.lampsystem.lampsystem.Repositories.RgbValuesPatternRepository;
import com.lampsystem.lampsystem.Repositories.PatternRepository;



@RestController
@RequestMapping("/rgb_values")
public class RgbValuesPatternController {

    @Autowired
    private RgbValuesPatternRepository rgbValuesPatternRepository;

    @Autowired
    private PatternRepository patternRepository;

    @GetMapping("/{id}")
    public RgbValuesPattern getRgbValuesPattern(@PathVariable(name = "id") long id, @RequestParam(required = false) String output) {
        RgbValuesPattern rgbValuesPattern = rgbValuesPatternRepository.findById(id);
        System.out.println(output);
        if (output == null) {
            rgbValuesPattern.setPattern(null);
        }

        return rgbValuesPattern;
    }

    @GetMapping("/update/{id}")
    public RgbValuesPattern getRgbValuesPatternUpdate(@PathVariable(name = "id") long id, @RequestHeader("Date") String date) throws InterruptedException {

        System.out.println(date);
        System.out.println(date.length());
        int c = (23 - date.length());
        for (int i = 0; i < c; i++) {
            date += '0';
        }

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss.SSS");
        LocalDateTime requestTime = LocalDateTime.parse(date.substring(0,23), formatter);

        System.out.println("request-time: " + requestTime.toString());

        RgbValuesPattern store = rgbValuesPatternRepository.findById(id);
        LocalDateTime storageTime = store.getLastUpdated().truncatedTo(ChronoUnit.MILLIS);
        System.out.println("stored-time: " + storageTime.toString());


        long startTime = System.currentTimeMillis();
        long elapsed;
        while (!requestTime.isBefore(storageTime)) {
            Thread.sleep(100);

            elapsed = System.currentTimeMillis() - startTime;
            if (elapsed > 28000) {
                return null;
            }

            rgbValuesPatternRepository.refresh(store);
            store = rgbValuesPatternRepository.findById(id);
            storageTime = store.getLastUpdated();
        }

        return store;
    }


    @PatchMapping("/{id}")
    public RgbValuesPattern updateRgbValuesPattern(@PathVariable(name = "id") RgbValuesPattern rgbValuesPattern, @RequestBody RgbValuesPattern new_rgbValuesPattern) {
        new_rgbValuesPattern.setRgbId(rgbValuesPattern.getRgbId());

        long patternId = new_rgbValuesPattern.getPatternId();
        long totalPattern = patternRepository.count();
        if (patternId < 1 || patternId > totalPattern) {
            return rgbValuesPattern;
        }

        new_rgbValuesPattern.setLastUpdated(LocalDateTime.now().truncatedTo(ChronoUnit.MILLIS));
        new_rgbValuesPattern.setPatternId(patternId);
        new_rgbValuesPattern.setPattern(new Pattern(patternId));
        return rgbValuesPatternRepository.save(new_rgbValuesPattern);
    }

    @PostMapping("")
    public RgbValuesPattern addRgbValuesPattern() {
        RgbValuesPattern rgbValuesPattern = new RgbValuesPattern(1, new int[]{0, 0, 0}, new Pattern(1), 1, LocalDateTime.now().truncatedTo(ChronoUnit.MILLIS));
        return rgbValuesPatternRepository.save(rgbValuesPattern);
    }

}