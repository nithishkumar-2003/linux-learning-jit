package com.example.gmsl.register.repo;

import com.example.gmsl.register.model.Register;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface RegisterRepository extends JpaRepository<Register, Long> {
    Optional<Register> findByName(String name);
}
