package com.example.gmsl.bitfield.model;

import jakarta.persistence.*;

@Entity
@Table(name = "bitfields")
public class Bitfield {
  @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;
  private String name;
  private int offset;
  private int width;
  private String description;

  public Bitfield(){}
  public Bitfield(String name, int offset, int width, String description) {
    this.name = name; this.offset = offset; this.width = width; this.description = description;
  }

  public Long getId() { return id; }
  public void setId(Long id) { this.id = id; }
  public String getName() { return name; }
  public void setName(String name) { this.name = name; }
  public int getOffset() { return offset; }
  public void setOffset(int offset) { this.offset = offset; }
  public int getWidth() { return width; }
  public void setWidth(int width) { this.width = width; }
  public String getDescription() { return description; }
  public void setDescription(String description) { this.description = description; }
}
