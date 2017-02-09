# zapalovac
Robot co chodí zapalovat svíčky na http://www.partezlin.cz/. 

Zapálení proběhne vždy s pravděpodobností 1/10. 


Cron nastavení:

```
0 * * * * python3 zapalovac/zapalovac.py
```
