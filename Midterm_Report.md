자동화된 식사 추천 시스템 (최종 업데이트)
프로젝트 설명
사용자가 입력한 재료와 개인 정보(키, 체중)를 바탕으로 요리를 추천하는 프로그램입니다.
냉장고에 있는 재료를 기반으로 다양한 레시피를 제안하며, 개인의 체중 및 신체 정보를 고려하여 맞춤형 식단을 제공합니다.
각 재료에 대한 칼로리를 포함하여 예상 음식 칼로리를 계산합니다.
프로젝트 요구 사항
사용자가 보유한 재료 입력 기능
키와 체중 입력 기능
평균 체중과 비교하여 식단 조절 권장 기능
기본 재료의 칼로리 정보 포함
예상 음식 칼로리 계산 기능
재료에 맞는 레시피 검색 기능
레시피 추천 및 요리 방법 제공
기능 세부 구현
재료 입력: 사용자가 현재 냉장고에 있는 재료를 입력합니다.
개인 정보 입력: 사용자가 자신의 키와 체중을 입력합니다.
평균 체중 비교:
BMI(체질량지수)를 계산하여 개인의 체중 상태를 평가합니다.
평균 BMI에 비해 차이가 많이 나면, 체중 조절을 위한 권장 식단을 제안합니다.
BMI 계산
BMI = 체중(kg) / (키(m) × 키(m)
BMI 기준에 따라:
저체중: BMI < 18.5
정상: 18.5 ≤ BMI < 24.9
과체중: 25 ≤ BMI < 29.9
비만: BMI ≥ 30


기본 재료의 칼로리 정보: 프로그램에 기본 재료의 칼로리 정보를 사전 정의합니다. (예:
사과: 52 kcal/100g
닭가슴살: 165 kcal/100g
브로콜리: 34 kcal/100g 등)
예상 음식 칼로리 계산:
사용자가 입력한 재료와 그 양에 따라 총 칼로리를 계산합니다.
레시피 추천: 입력된 재료를 기반으로 가능한 레시피를 검색하여 추천합니다.
요리 방법 출력: 추천된 레시피의 조리 방법과 소요 시간을 출력합니다.
식단 조절 권장: 체중 조절이 필요한 경우, 칼로리 섭취량과 영양소 비율을 고려하여 맞춤형 레시피를 제안합니다.

역할 
김태훈(Theodore): 코드 작성 (전체적 틀 구성, 문제 확인 ) 
심미지(Miji): 코드 작성 (조건문, 함수) 
정민서(Matthew):코드 작성 (print, variables) 



import json


calories_data = {
    '사과': 52,
    '닭가슴살': 165,
    '브로콜리': 34,
    '밥': 130,
    '계란': 155,
    '소고기': 250.5,
    '돼지고기': 241.1,
}


recipes_data = {
    '사과 샐러드': ['사과', '브로콜리'],
    '닭가슴살 샐러드': ['닭가슴살', '브로콜리'],
    '소고기 덮밥': ['소고기', '밥', '브로콜리'],
    '계란 볶음밥': ['계란', '밥'],
    '돼지고기 스테이크': ['돼지고기', '브로콜리']
}


def get_user_info():
    try:
        height = float(input("키를 입력하세요 (cm): ")) / 100  
        weight = float(input("체중을 입력하세요 (kg): "))
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        return get_user_info()  
    return height, weight


def calculate_bmi(height, weight):
    print("여기서 잠깐!! BMI란 신체의 지방 비율을 추정하는 방법으로, 체중과 키를 기반으로 계산됩니다!")
    return weight / (height ** 2)


def get_ingredients_and_calories():
    total_calories = 0
    ingredients = {}
    
    while True:
        ingredient = input("재료를 입력하세요 (끝내려면 '끝' 입력): ").strip().lower()  
        if ingredient == '끝':
            break
        amount = input(f"{ingredient}의 양을 입력하세요 (g): ")
        
        try:
            amount = float(amount)
        except ValueError:
            print("잘못된 양입니다. 숫자를 입력해주세요.")
            continue
        
        if ingredient in calories_data:
            calories = (calories_data[ingredient] * amount) / 100
            total_calories += calories
            ingredients[ingredient] = (amount, calories)
        else:
            print("이 재료는 데이터베이스에 없습니다.")
    
    return ingredients, total_calories


def suggest_recipes(available_ingredients):
    print("\n사용할 수 있는 재료로 만들 수 있는 요리:")
    recommended_recipes = []
    
    for recipe, ingredients in recipes_data.items():
        if all(ingredient in available_ingredients for ingredient in ingredients):
            recommended_recipes.append(recipe)
    
    if recommended_recipes:
        for recipe in recommended_recipes:
            print(f"- {recipe}")
    else:
        print("사용할 수 있는 재료로 만들 수 있는 요리가 없습니다.")

def recommend_recipes(ingredients):
    print("\n입력된 재료:")
    if not ingredients:
        print("입력된 재료가 없습니다.")
        return
    for ingredient, (amount, calories) in ingredients.items():
        print(f"{ingredient}: {amount}g - {calories:.2f} kcal")
    
    
    available_ingredients = [ingredient for ingredient in ingredients]
    
    
    suggest_recipes(available_ingredients)


def save_user_info_to_json(height, weight, filename='user_info.json'):
    user_data = {
        'height': height,
        'weight': weight
    }
    with open(filename, 'w') as json_file:
        json.dump(user_data, json_file)
    print(f"사용자 정보가 {filename}에 저장되었습니다.")


def main():
    print("자동화된 식사 추천 시스템에 오신 것을 환영합니다!")
    
    height, weight = get_user_info()
    bmi = calculate_bmi(height, weight)
    print(f"당신의 BMI는 {bmi:.2f}입니다.")

    
    save_user_info_to_json(height, weight)
    
   
    ingredients, total_calories = get_ingredients_and_calories()
    print(f"총 칼로리: {total_calories:.2f} kcal")
    
   
    recommend_recipes(ingredients)

if __name__ == "__main__":
    main()


이 코드는 사용자의 키와 몸무게 정보를 입력받고 사용자의 BMI를 알려준다. 그리고 미리 입력해둔 재료와 칼로리를 바탕으로 원하는 재료에 맞는 레시피를 알려준다.

먼저 Import json은 javascript object notation으로 데이터를 교환하는 형식이다. (데이터 통신)
calories_data는 딕셔너리 형식으로 만들어 key 값에는 음식들이 저장되어 있고, value 부분엔 그 음식의 칼로리가 저장되어 있다.
recipes_data는 재료를 보고 레시피를 추천해 줄 수 있게끔 레시피 목록을 적어놓은 것이다
(재료나 레시피는 원하면 더 추가 가능!)
def_user_info 함수는 먼저 키와 체중을 입력받는다 키는 Meter로 저장시키기 위해 100으로 나누고, 무게는 그대로 쓰인다. 숫자가 아닌 다른 것을 입력했을 시에는 “잘못된 입력입니다. 숫자를 입력해 주세요.”라는 문구가 뜨고 다시 돌아가서 숫자를 입력할 수 있게 된다.
유저 입력을 다 받으면 그 정보들을 바탕으로 BMI(체지방률)을 계산하여 바로 알려준다.
get_ingredients_and_calories는 처음에는 아무 정보가 없으므로 총 칼로리와 ingredient를 0으로 지정한다. while True 부분에선 동작하고 있을 때 ingredient는 재료를 엔터를 누르면 그램 수를 입력할 수 있으며 또다시 엔터를 누르면 새로운 재료 입력이 가능하게끔 뜬다. 원할 때까지 재료를 입력할 수 있으며 다 입력했을 때 “끝”이라고 입력하면 끝난다. 잘못된 양을 입력했을 시에 “잘못된 양입니다. 숫자를 입력해 주세요.”라고 뜨며 다시 입력을 할 수 있게 된다.
return indegrients, total_calories는 부분은 칼로리와 양을 바탕으로 값을 적은 것이다.
def suggest_recipes는 recommended_recipes라는 함수를 활용해 내가 가지고 있는 재료를 다 쓰는 레시피가 있을 경우 그 레시피를 추천해 주고 만약에 없다면 “사용할 수 있는 재료로 만들 수 있는 요리가 없습니다.”라고 뜬다.
def save_your_info_to_jason은 사용자 정보의 데이터를 jason이라는 정보함수에 저장을 해준다.
def main은 처음에 “자동화된 식사 추천 시스템에 오신 것을 환영합니다.”라고 뜨며, 몸무게와 키의 정보를 유저에게 받고 그걸 바탕으로 BMI 함수 계산을 프린트해준다. 그리고 총 칼로리들을 모두 불러와 몇인지를   알려주고 함수를 불러와 레시피를 불러준다.
마지막으로 if __name__==”__main__”는 특정 코드 블록을 프로그램의 진입점으로 설정하는 역할을 합니다. 이를 통해 해당 파일이 직접 실행될 때만 main() 함수를 호출하고, 다른 파일에서 이 파일을 모듈로 불러올 때는 main() 함수가 자동으로 실행되지 않도록 합니다.

def 나 main 함수는 우리가 직접 틀을 잡고 직점 짰으며 BMI처럼 코드 안에 계산하는 부분은 ChatGPT에게 물어보았다.




