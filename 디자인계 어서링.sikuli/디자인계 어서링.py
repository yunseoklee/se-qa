scroll = "1603423325777.png"
components = "1603417268616.png"
filter = "1603420662856.png"
columns_container = "1603420932287.png"
drag_components = "1603420959280.png"
inner = "1603423623185.png"
feature_item = "1603423639057.png"
inner_item = "1603429044900.png"
configure = "1603429274406.png"

openApp("C:\Program Files (x86)\Google\Chrome\Application/Chrome.exe http://52.79.182.113:4512/editor.html/content/samsung/ve/wdc/qa/psm/home-template/test.html")
sleep(10)
click(components)
wait(1)
wheel(scroll, WHEEL_DOWN, 6)
# 마우스가 이미지 위로 이동한 후 wheel을 6만큼 내림
click(filter)
type('columns container')
# 키보드 영어로 설정해야 정상 입력됨
type(Key.ENTER)
dragDrop(columns_container,drag_components)
# 첫번 째 요소를 두번 째 요소로 이동시킴
sleep(10)
wheel(scroll, WHEEL_DOWN, 6)
wait(1)
doubleClick(inner)
click(feature_item)
sleep(10)
wheel(scroll, WHEEL_DOWN, 6)
wait(1)
click(inner_item)
click(configure)
# 컴포넌트 open 까지 완료
click("1603435573537.png")
click("1603435592748.png")
click("1603435635333.png")
type("galaxy")
type(Key.ENTER)
wait(1)
wheel("1603435707515.png", WHEEL_DOWN, 3)
dragDrop("1603436915856.png","1603435765067.png")
click("1603435782199.png")
sleep(10)
wheel(scroll, WHEEL_DOWN, 6)
# 이미지 어서링
click("1603876226859.png")
click("1603876244821.png")
sleep(10)
wheel(scroll, WHEEL_DOWN, 6)
