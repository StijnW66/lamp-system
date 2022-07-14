package com.lampsystem.lampsystem.Controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.*;
import com.lampsystem.lampsystem.Entities.Pattern;
import com.lampsystem.lampsystem.Repositories.PatternRepository;


@RestController
@RequestMapping("/pattern")
public class PatternController {

    @Autowired
    private PatternRepository patternRepository;


    @GetMapping
    public List<Pattern> getPattern() {
        List<Pattern> result = patternRepository.findAll();
        Collections.sort(result);
        return result;
    }

    @GetMapping("/{id}")
    public Pattern getPatternById(@PathVariable(name = "id") long id) {
        return patternRepository.findById(id);
    }

    @GetMapping("/count")
    public long getPatternCount() {
        return patternRepository.count();
    }

    @PostMapping("")
    public Pattern addPattern(@RequestBody Pattern pattern) {
        return patternRepository.save(pattern);
    }

    @PatchMapping("/{id}")
    public Pattern updatePattern(@PathVariable(name = "id") Pattern pattern, @RequestBody Pattern new_pattern) {
        new_pattern.setPatternId(pattern.getPatternId());
        return patternRepository.save(new_pattern);
    }

    @DeleteMapping("/{id}")
    public void deletePatternById(@PathVariable(name = "id") Pattern pattern) {
        patternRepository.delete(pattern);
    }

}