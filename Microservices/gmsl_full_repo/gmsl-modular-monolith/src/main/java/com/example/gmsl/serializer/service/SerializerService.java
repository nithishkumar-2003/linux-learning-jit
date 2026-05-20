package com.example.gmsl.serializer.service;

import com.example.gmsl.register.model.Register;
import com.example.gmsl.register.service.RegisterService;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class SerializerService {
  private final RegisterService registerService;

  public SerializerService(RegisterService registerService) {
    this.registerService = registerService;
  }

  public List<Register> getRegistersForSerializer(Long serializerId) {
    return registerService.listAll();
  }

  public Register writeRegister(Long regId, Long value) {
    return registerService.updateValue(regId, value);
  }
}
