# NonLifeInsurance

## alembicのコマンド
* Migration
```  
  alembic revision --autogenerate -m "create tables"
```
* upgrade DBへの適用  
```
alembic upgrade head
```