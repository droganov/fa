Generating keys

```python
from scripts.generate_key import generate_key


print(f'A256GCM_KEY="{generate_key(32)}"')
print(f'JWT_SECRET_KEY="{generate_key(64)}"')
print(f'SESSION_SECRET_KEY="{generate_key(88)}"')
print(f'SESSION_SALT="{generate_key(64)}"')
```
