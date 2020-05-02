package com.item.autoconfig.autoconfig;

import com.dangdang.ddframe.job.reg.base.CoordinatorRegistryCenter;
import com.dangdang.ddframe.job.reg.zookeeper.ZookeeperConfiguration;
import com.dangdang.ddframe.job.reg.zookeeper.ZookeeperRegistryCenter;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * 自动配置类
 * 当配置文件有值的时候加载
 * @author zcm
 */
@Configuration
@ConditionalOnProperty("elasticjob.zookeeper.server-list")
@EnableConfigurationProperties(ZookeeperPorperties.class)
@RequiredArgsConstructor(onConstructor = @__(@Autowired))
public class ZookeeperAutoConfig {

   final ZookeeperPorperties zookeeperPorperties;

    @Bean(initMethod = "init")
    public CoordinatorRegistryCenter zkCenter(){
        ZookeeperConfiguration configuration = new ZookeeperConfiguration(zookeeperPorperties.getServerList(), zookeeperPorperties.getNamespace());
        return new ZookeeperRegistryCenter(configuration);
    }

}
