package com.lampsystem.lampsystem.Entities;

import javax.persistence.*;
import java.time.LocalDateTime;
import com.lampsystem.lampsystem.Entities.*;



@Entity
public class RgbValuesPattern {

    @Id
    private long rgbId;

    private int[] rgb;

    @ManyToOne
    @JoinColumn(name = "pattern")
    private Pattern pattern;

    private long patternId;

    LocalDateTime last_updated;

    public RgbValuesPattern() {

    }


    public RgbValuesPattern(long id, int[] rgb, Pattern pattern, long patternId, LocalDateTime date) {
        this.rgbId = id;
        this.rgb = rgb;
        this.pattern = pattern;
        this.patternId = patternId;
        this.last_updated = date;
    }

    public long getRgbId() {
        return rgbId;
    }

    public int[] getRgb() {
        return rgb;
    }

    public Pattern getPattern() {
        return pattern;
    }

    public long getPatternId() {
        return patternId;
    }

    public void setRgbId(long rgbId) {
        this.rgbId = rgbId;
    }

    public LocalDateTime getLastUpdated() {
        return last_updated;
    }

    public void setLastUpdated(LocalDateTime last_updated) {
        this.last_updated = last_updated;
    }

    public void setPattern(Pattern pattern) { this.pattern = pattern; }
    public void setPatternId(long patternId) { this.patternId = patternId; }
}
