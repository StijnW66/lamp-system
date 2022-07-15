package com.lampsystem.lampsystem.Repositories;


import org.springframework.data.domain.*;
import org.springframework.data.repository.*;
import com.lampsystem.lampsystem.Entities.Pattern;
import org.springframework.data.jpa.repository.JpaRepository;



public interface PatternRepository extends JpaRepository<Pattern, Long> {

    Pattern findById(long id);

}