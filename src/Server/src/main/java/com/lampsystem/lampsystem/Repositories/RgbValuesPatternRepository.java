package com.lampsystem.lampsystem.Repositories;


import org.springframework.data.domain.*;
import org.springframework.data.repository.*;
import com.lampsystem.lampsystem.Entities.RgbValuesPattern;
import org.springframework.data.jpa.repository.JpaRepository;
import com.lampsystem.lampsystem.Repositories.CustomRepository;








public interface RgbValuesPatternRepository extends CustomRepository<RgbValuesPattern, Long> {

	RgbValuesPattern findById(long id);

}