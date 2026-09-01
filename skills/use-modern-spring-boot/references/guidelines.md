# Spring Boot version rules

Resolve the Boot, Spring Framework, Java, and dependency-management versions
from the build before using a feature. Do not mix examples from different Boot
generations or silently change the web stack.

## Generation gates

- Spring Boot 3 and later use Jakarta EE namespaces and bean-based Spring
  Security configuration. Treat `javax.*` imports and
  `WebSecurityConfigurerAdapter` examples as older-generation migration
  material, not new-code templates.
- Spring Boot 4 targets require Java 17 or later and Spring Framework 7 APIs.
  Resolve the Boot dependency-management platform and Java toolchain together
  before using those APIs.

## Configuration and operations

- Prefer type-safe configuration properties for related settings and validate
  them at startup when invalid configuration would make the service unsafe.
- Use Actuator and Micrometer's observation model when the project has an
  observability requirement; avoid high-cardinality tags.
- For native images, check reflection, proxy, and resource requirements instead
  of assuming JVM reflection will work unchanged.

## Modern Spring boundaries

- Use `jakarta.*` APIs and bean-based security configuration on current Boot
  lines. Treat `javax.*` imports and `WebSecurityConfigurerAdapter` examples as
  migration material, not templates for new code.

## Concurrency

- Virtual threads require a compatible JDK and may change thread-pool and
  scheduler behavior. Enable them only with an explicit workload decision and
  validate pinned-thread and shutdown behavior.
- WebFlux code must remain non-blocking end to end, or isolate blocking work
  with a deliberate scheduler boundary.

## Authority

- https://docs.spring.io/spring-boot/reference/
- https://docs.spring.io/spring-boot/reference/features/spring-application.html
- https://docs.spring.io/spring-boot/reference/actuator/observability.html
- https://docs.spring.io/spring-boot/reference/web/reactive.html
- https://docs.spring.io/spring-security/reference/
