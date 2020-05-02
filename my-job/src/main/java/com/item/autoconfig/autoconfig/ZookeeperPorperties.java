package com.item.autoconfig.autoconfig;

import lombok.Getter;
import lombok.Setter;
import org.springframework.boot.context.properties.ConfigurationProperties;

/**
 * @author zcm
 */
@ConfigurationProperties(prefix = "elasticjob.zookeeper")
@Getter
@Setter
public class ZookeeperPorperties {

    private String serverList;

    private String namespace;
}
