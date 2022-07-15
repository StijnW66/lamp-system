package com.lampsystem.lampsystem;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import com.lampsystem.lampsystem.Repositories.CustomRepositoryImpl;

@SpringBootApplication
@EnableJpaRepositories (repositoryBaseClass = CustomRepositoryImpl.class)
public class LampSystemApplication {

	public static void main(String[] args) {
		SpringApplication.run(LampSystemApplication.class, args);
	}

}
