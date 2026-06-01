package com.example.gmsl.register.model;

import jakarta.persistence.*;

@Entity
@Table(name = "registers")
public class Register {
  @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;
  private String name;
  private String address;
  private Long value;

  public Register(){}

  public Register(String name, String address, Long value) {
    this.name = name;
    this.address = address;
    this.value = value;
  }

  public Long getId() { return id; }
  public void setId(Long id) { this.id = id; }
  public String getName() { return name; }
  public void setName(String name) { this.name = name; }
  public String getAddress() { return address; }
  public void setAddress(String address) { this.address = address; }
  public Long getValue() { return value; }
  public void setValue(Long value) { this.value = value; }
}
