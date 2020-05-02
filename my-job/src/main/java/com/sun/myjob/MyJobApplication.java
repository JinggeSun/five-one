package com.sun.myjob;

import com.ulisesbocchio.jasyptspringboot.annotation.EnableEncryptableProperties;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @author zcm
 */
@SpringBootApplication
@MapperScan(value="com.sun.myjob.mapper")
@EnableEncryptableProperties
public class  MyJobApplication {

	public static void main(String[] args) {
		SpringApplication.run(MyJobApplication.class, args);
	}

}
