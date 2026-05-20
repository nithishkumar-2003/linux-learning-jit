# gmsl-modular-monolith

A single Spring Boot modular monolith (Java 17) that exposes APIs for Registers, Bitfields and Serializers.
Run with:

    mvn spring-boot:run

APIs:
- GET /api/registers
- POST /api/registers/{id}/write  { "value": 123 }
- GET /api/serializers/{id}/registers
- GET /api/bitfields

H2 console: http://localhost:8080/h2-console  (jdbc:h2:mem:gmsldb)
