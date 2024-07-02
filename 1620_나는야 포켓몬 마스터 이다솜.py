n, m = map(int, input().split())
pokemon_dict = dict()  # 번호 -> 포켓몬 이름
pokemon_name_dict = dict()  # 포켓몬 이름 -> 번호

for i in range(1, n + 1):
    i_str = str(i)
    pokemon = input()
    pokemon_dict[i_str] = pokemon
    pokemon_name_dict[pokemon] = i_str

result = []
for i in range(m):
    ans = input()
    if ans.isdigit():  # ans가 숫자인 경우
        res = pokemon_dict.get(ans)
    else:  # ans가 포켓몬 이름인 경우
        res = pokemon_name_dict.get(ans)
    
    if res is not None:
        result.append(res)

for elem in result:
    print(elem)
