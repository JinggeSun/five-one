package com.sun.myjob.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 *
 * @author sunjg
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class GsipIndex {

  private long id;
  private String indexName;
  private String indexDesc;

}
