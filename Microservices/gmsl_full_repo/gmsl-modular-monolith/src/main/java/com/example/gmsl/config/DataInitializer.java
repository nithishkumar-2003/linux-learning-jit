package com.example.gmsl.config;

import com.example.gmsl.bitfield.model.Bitfield;
import com.example.gmsl.bitfield.repo.BitfieldRepository;
import com.example.gmsl.register.model.Register;
import com.example.gmsl.register.repo.RegisterRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DataInitializer {

  @Bean
  CommandLineRunner init(RegisterRepository registerRepo, BitfieldRepository bitfieldRepo) {
    return args -> {
      registerRepo.save(new Register("REG_CTRL", "0x100", 0L));
      registerRepo.save(new Register("REG_STATUS", "0x104", 0L));
      bitfieldRepo.save(new Bitfield("ENABLE_TX", 0, 1, "Enable transmitter"));
      bitfieldRepo.save(new Bitfield("MODE_SELECT", 1, 2, "Mode selection"));
    };
  }
}
