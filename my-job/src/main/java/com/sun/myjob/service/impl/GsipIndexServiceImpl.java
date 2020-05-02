package com.sun.myjob.service.impl;

import com.sun.myjob.entity.GsipIndex;
import com.sun.myjob.mapper.GsipMapper;
import com.sun.myjob.service.GsipIndexService;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author zcm
 */
@Service
@RequiredArgsConstructor(onConstructor = @__(@Autowired))
public class GsipIndexServiceImpl implements GsipIndexService {

    final GsipMapper mapper;

    @Override
    public List<GsipIndex> list() {
        return mapper.selectList(null);
    }
}
