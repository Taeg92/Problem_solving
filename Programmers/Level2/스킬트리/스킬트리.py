def check(skill, spell):
    for i in range(len(skill)):
        if i < len(spell):
            if skill[i] != spell[i]:
                return False
    return True

def solution(skill, skill_trees):
    answer = 0
    for spell in skill_trees:
        for s in spell:
            if s not in skill:
                spell = spell.replace(s, '')
        if check(skill, spell):
            answer += 1
                
    return answer

skill = 'CBD'
skill_trees = 	["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))