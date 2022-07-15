package com.lampsystem.lampsystem.Entities;

import javax.persistence.*;

@Entity
public class Pattern implements Comparable<Pattern> {

    @Id
    @GeneratedValue
    private long patternId;
    private int[][] patternContents;
    private String name;

    public Pattern() {

    }

    public Pattern(long patternId) {
        this.patternId = patternId;
    }

    public Pattern(int[][] patternContents, String name) {
        this.patternContents = patternContents;
        this.name = name;
    }

    public long getPatternId() {
        return patternId;
    }

    public int[][] getPatternContents() {
        return patternContents;
    }

    public String getName() {
        return name;
    }

    public void setPatternId(long patternId) {
        this.patternId = patternId;
    }

    @Override
    public int compareTo(Pattern u) {
        return (int) (getPatternId() - u.getPatternId());
    }
}