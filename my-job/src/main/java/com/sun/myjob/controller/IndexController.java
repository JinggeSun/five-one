package com.sun.myjob.controller;

import com.sun.myjob.mapper.GsipMapper;
import com.sun.myjob.service.GsipIndexService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author zcm
 */
@RestController
public class IndexController {

    @Autowired
    GsipIndexService service;

    @GetMapping("/")
    public String index(){
        System.out.println(service.list());
        return "success";
    }
}
