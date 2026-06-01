GMSL Full Repo (generated)

Contents:
- gmsl-modular-monolith/   -> Fully working modular monolith Spring Boot app (H2). Run with `mvn spring-boot:run`.
- gmsl-multi-module/      -> Maven multi-module skeleton (placeholder modules).
- frontend-vite/          -> Minimal Vite React frontend that calls the monolith API.

How to run:
1) Run the backend monolith:
   cd gmsl-modular-monolith
   mvn spring-boot:run

2) Open the APIs:
   - GET http://localhost:8080/api/registers
   - GET http://localhost:8080/api/bitfields
   - GET http://localhost:8080/api/serializers/1/registers

3) Run the frontend:
   cd frontend-vite
   npm install
   npm run dev

Download: gmsl_full_repo.zip
