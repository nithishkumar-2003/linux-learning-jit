package com.example.gmsl.register.service;

import com.example.gmsl.register.model.Register;
import com.example.gmsl.register.repo.RegisterRepository;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class RegisterService {
  private final RegisterRepository repo;
  public RegisterService(RegisterRepository repo) { this.repo = repo; }

  public List<Register> listAll() { return repo.findAll(); }
  public Register get(Long id) { return repo.findById(id).orElse(null); }
  public Register create(Register r) { return repo.save(r); }
  public Register updateValue(Long id, Long newValue) {
    Register r = repo.findById(id).orElseThrow();
    r.setValue(newValue);
    return repo.save(r);
  }
}
