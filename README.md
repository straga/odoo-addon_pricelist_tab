odoo-addon-our_pricelist_tab
============================

Add PriceList tab in product


video - https://www.youtube.com/watch?v=UnJDuE5DVeo


**Price List - формирования цены / odoo 8.0**

В модуле Pricelist можно формировать цены. Нас интересует зависиместь цены от количества.

Для примера добим три продукта.
(Warehouse -> Product)

    Maketesana A4 - Ед.изм. = unit - Цена ставиться в Product-Product за единицу.
    Izciršana 2 - Ед.изм. = blank - Цена ставиться в PriceListe зависит от заготовок.
    Salimešana - Ед.изм. = circulation Цена ставиться в PriceListe зависит от тиража.

Количество от большего к меньшему, регулируется последовательностью(sequances), тогда система проверяет количества в PriceListe при продажи и ставит соответствующую цену.

    Salimešana - Ед.изм. = circulation - Цена ставиться в PriceListe зависит от тиража.
    1500 - 0.0441
    1250 - 0.0464
    1500 - 0.0488

    897 3-cir-1500 [3] Salimešana 1 shov 1500 Public Price
    898 3-cir-1250 [3] Salimešana 1 shov 1250 Public Price
    899 3-cir-1000 [3] Salimešana 1 shov 1000 Public Price

Но если все это добавлять в PriceList Versions – получается не удобно. 


**Module Pricelist_tab – закладка Prices продуктах**

В закладке мы можем видеть в каких Праислистах участвует продукт.
Праислист может быть назначен продукту и категории.

Прямо из Продуктов можно добавлять цены.



**Wizard Add Price for circulation and blanks**
    


    
[[Circulation-Blank]] - Тираж и Заготовки

Circulation

seq rule name price_version min_quan

    80 от 1500 - до 1750 cir. Manufacture ver.1.0 1500
    90 от 1250 - до 1500 cir. Manufacture ver.1.0 1250
    100 от 1000 - до 1250 cir. Manufacture ver.1.0 1000


Кнопка / wizard. Которая позволит добавлять количества из шаблона. для тиража либо для заготовок.

На закладке (Prices) кнопка "Add Price". По нажатию кнопки открывается wizard окно. Выбираем версию Pricelist и тип(тираж или заготовки)
Жмём ок и добавляются записи от ... до ... .
Остаётся только добавить цены к этим позициям.

Сами данные для шаблона лежат в Sale->Pricelists Tab->Res.ext Config
