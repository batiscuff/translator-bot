<h1 align="center">Бот переводчик
<p align="center">
<img src="https://hatscripts.github.io/circle-flags/flags/ua.svg" width="38" height="34"> <img src="img/sort-swap-svgrepo-com.svg" widht="34" height="32" /> <img src="https://hatscripts.github.io/circle-flags/flags/cz.svg" width="38" height="34">
</p></h1>


<h3>Описание</h3>
<p>Мой первый бот на <a href="https://github.com/aiogram/aiogram/">aiogram</a>. Пример конфигурации бота находится в <code>.env.dist</code>. В качестве главного переводчика взят <a href="https://slovnik.seznam.cz/">slovnik.seznam</a>, а для перевода с украинского на русский используется GoogleTranslator из библиотеки deep_translate<i>(есть в requirements.txt)</i>.
</p>



### Использование
⚠️ <strong>Перед использованием нужно создать файл `.env` и прописать в нём токен бота и id администратора <i>(так как это сделано в `.env.dist`)</i></strong>
```sh
git clone http://github.com/batiscuff/translator-bot
cd translator-bot && pip3 install -r requirements.txt 
python3 -m app -s
```
Если что-то пошло не так попробуйте запустить бота командой: `python3 -m app -h` что бы увидить доступные параметры запуска.