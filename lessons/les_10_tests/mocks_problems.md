Представьте еще раз, что ваш код делает запрос к внешнему API. 
В этом случае внешней зависимостью является API, который может быть изменен без вашего согласия.

Если внешняя зависимость изменит свой интерфейс, ваши фиктивные объекты Python станут недействительными. 
Если это произойдет (и изменение интерфейса является критическим), ваши тесты будут пройдены, 
потому что ваши фиктивные объекты замаскировали изменение, но ваш производственный код завершится ошибкой.

К сожалению, это не та проблема, unittest.mockдля которой предусмотрено решение. 
Вы должны проявлять рассудительность, когда имитируете внешние зависимости.

Now, you’re able to:
- Use Mock to imitate objects in your tests
- Check usage data to understand how you use your objects
- Customize your mock objects’ return values and side effects
- patch() objects throughout your codebase
- See and avoid problems with using Python mock objects

https://realpython.com/python-mock-library/