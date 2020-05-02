package com.sun.myjob.config;

import org.jasypt.encryption.StringEncryptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.ApplicationContext;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Component;

@Component
public class TestPwd implements CommandLineRunner {

    @Autowired
    ApplicationContext applicationContext;

    @Autowired
    StringEncryptor stringEncryptor;

    @Override
    public void run(String... args) throws Exception {

        Environment environment = applicationContext.getBean(Environment.class);

        String mysqlOriginPswd = environment.getProperty("spring.datasource.password");

        System.out.println( "MySQL原始明文密码为：" + mysqlOriginPswd );

        String mysqlEncryptedPswd = encrypt( mysqlOriginPswd );

        System.out.println( "MySQL原始明文密码加密后的结果为：" + mysqlEncryptedPswd );


    }

    private String encrypt( String originPassord ) {
        String encryptStr = stringEncryptor.encrypt( originPassord );
        return encryptStr;
    }

    private String decrypt( String encryptedPassword ) {
        String decryptStr = stringEncryptor.decrypt( encryptedPassword );
        return decryptStr;
    }
}
