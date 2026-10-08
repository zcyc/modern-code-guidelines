# Spring Boot

## Generation gates

- Boot 3+ uses Jakarta EE namespaces and bean-based Security configuration; older javax/WebSecurityConfigurerAdapter examples are migration material.
- Boot 4 requires Java 17+ and Spring Framework 7; use its dependency-management line instead of mixing framework generations.

## Injection, transactions and execution

- Constructor injection and validated ConfigurationProperties express dependencies/configuration; keep invalid required settings as startup failures.
- Transaction boundaries protect business operations; proxy annotations do not intercept self-invocation. Preserve established validation/security/error contracts.
- MVC/blocking and WebFlux/reactive have different execution models. Isolate blocking I/O from reactive pipelines through a deliberate scheduler boundary.
- Virtual threads require matching JDK/workload support; measure benefit, pinning and shutdown. Scarce resources still need bounds.
- Actuator/Micrometer serve operational requirements with low-cardinality tags. Native images need explicit reflection/proxy/resource and library compatibility checks.

## Sources

- https://docs.spring.io/spring-boot/reference/
- https://docs.spring.io/spring-boot/reference/features/spring-application.html
- https://docs.spring.io/spring-boot/reference/actuator/observability.html
- https://docs.spring.io/spring-boot/reference/web/reactive.html
- https://docs.spring.io/spring-security/reference/
