package com.example.gmsl.api;

import com.example.gmsl.bitfield.repo.BitfieldRepository;
import com.example.gmsl.register.model.Register;
import com.example.gmsl.register.service.RegisterService;
import com.example.gmsl.serializer.service.SerializerService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class ApiController {

  private final RegisterService registerService;
  private final SerializerService serializerService;
  private final BitfieldRepository bitfieldRepo;

  public ApiController(RegisterService registerService,
                       SerializerService serializerService,
                       BitfieldRepository bitfieldRepo) {
    this.registerService = registerService;
    this.serializerService = serializerService;
    this.bitfieldRepo = bitfieldRepo;
  }

  @GetMapping("/registers")
  public List<Register> listRegisters() { return registerService.listAll(); }

  @GetMapping("/registers/{id}")
  public ResponseEntity<Register> getRegister(@PathVariable Long id) {
    Register r = registerService.get(id);
    return r == null ? ResponseEntity.notFound().build() : ResponseEntity.ok(r);
  }

  @PostMapping("/registers")
  public Register createRegister(@RequestBody Register r) {
    return registerService.create(r);
  }

  @PostMapping("/registers/{id}/write")
  public ResponseEntity<Register> writeRegister(@PathVariable Long id, @RequestBody Map<String,Long> body) {
    Long val = body.get("value");
    try {
      Register updated = registerService.updateValue(id, val);
      return ResponseEntity.ok(updated);
    } catch (Exception e) {
      return ResponseEntity.notFound().build();
    }
  }

  @GetMapping("/serializers/{id}/registers")
  public List<Register> getSerializerRegisters(@PathVariable Long id) {
    return serializerService.getRegistersForSerializer(id);
  }

  @PostMapping("/serializers/{id}/registers/{regId}/write")
  public ResponseEntity<Register> writeSerializerRegister(@PathVariable Long id, @PathVariable Long regId, @RequestBody Map<String,Long> body) {
    Long val = body.get("value");
    try {
      Register updated = serializerService.writeRegister(regId, val);
      return ResponseEntity.ok(updated);
    } catch (Exception e) {
      return ResponseEntity.badRequest().build();
    }
  }

  @GetMapping("/bitfields")
  public ResponseEntity<?> listBitfields() {
    return ResponseEntity.ok(bitfieldRepo.findAll());
  }
}
