from django.shortcuts import render
from django.views.generic import TemplateView
import copy

# Create your views here.


class FleriCalc(TemplateView):
    template_name_get = 'calc/fleri_calc_orient.html'
    template_name_post = 'calc/fleri_calc_orient_result.html'
    template_name_error = 'calc/fleri_calc_orient_error.html'

    def get(self, request):
        return render(request, self.template_name_get)

    def post(self, request):
        not_parsed_graph = request.POST['graph']
        list_of_not_parsed_strings = not_parsed_graph.splitlines()

        for i in range(len(list_of_not_parsed_strings) - 1, -1, -1):
            list_of_not_parsed_strings[i] = list_of_not_parsed_strings[i].replace(' ', '')
            if list_of_not_parsed_strings[i] == '':
                del list_of_not_parsed_strings[i]

        edges = []

        for i in list_of_not_parsed_strings:
            edges.append(i.split('>'))

        if len(edges) == 0:
            return render(request, self.template_name_error,
                          context={'msg': 'Рекомендуем нажать "Назад" и попробовать снова.'})

        for i in edges:
            if len(i) != 2:
                return render(request, self.template_name_error)
            if len(i[0]) == 0 or len(i[1]) == 0:
                return render(request, self.template_name_error)
            i.append(i[0]+'->'+i[1]) #по индексу 2 строка для ребра диграфа
            i.append('')#по индексу 3 строка для стиля ребра диграфа
            i.append(True)#по индексу 4 узнаём пройдено ли ребро


        d = dict()
        for i in edges:
            if not i[0] in d.keys():
                d[i[0]] = 1
            else:
                d[i[0]] += 1
            if not i[1] in d.keys():
                d[i[1]] = -1
            else:
                d[i[1]] -= 1

        for i in d.values():
            if i != 0:
                return render(request, self.template_name_error,
                              context={'msg': 'Граф не является эйлеровым'})


        g = make_digraph(edges)
        data = []
        it = 1
        v_len = len(d.values())
        deal = len(edges) + 1
        v = edges[0][0]
        ans = '(' + str(v) + ')'

        while it != deal:
            OK_edges = []
            for i in edges:
                if i[4]:
                    i[3] = ''
                else:
                    i[3] = '[color=grey]'

            for i in range(0, len(edges)):
                if edges[i][0] == v and edges[i][4]:
                    OK_edges.append([i, False])

            not_find_true = True

            for i in OK_edges:
                visited = dict()
                for q in d.keys():
                    visited[q] = False
                i[1] = dfs_or_leave(edges, visited, edges[i[0]][1], edges[i[0]][0])
                if not i[1]:
                    edges[i[0]][3] = '[color=red,penwidth=5.0]'
                elif not_find_true:
                    not_find_true = False
                    edges[i[0]][3] = '[color=green,penwidth=5.0]'
                    edges[i[0]][4] = False
                    v = edges[i[0]][1]
                    ans += '(' + str(v) + ')'
                else:
                    edges[i[0]][3] = '[color=yellow,penwidth=5.0]'
            data.append([it, make_digraph(edges)])
            it += 1

        count = len(data)
        args = {'data': data, 'count': count, 'ans': ans}

        return render(request, self.template_name_post, args)


class HerhCalc(TemplateView):
    template_name_get = 'calc/herh_calc_orient.html'
    template_name_post = 'calc/herh_calc_orient_result.html'
    template_name_error = 'calc/herh_calc_orient_error.html'

    def get(self, request):
        return render(request, self.template_name_get)

    def post(self, request):
        not_parsed_graph = request.POST['graph']
        list_of_not_parsed_strings = not_parsed_graph.splitlines()

        for i in range(len(list_of_not_parsed_strings) - 1, -1, -1):
            list_of_not_parsed_strings[i] = list_of_not_parsed_strings[i].replace(' ', '')
            if list_of_not_parsed_strings[i] == '':
                del list_of_not_parsed_strings[i]

        edges = []

        for i in list_of_not_parsed_strings:
            edges.append(i.split('>'))

        if len(edges) == 0:
            return render(request, self.template_name_error,
                          context={'msg': 'Рекомендуем нажать "Назад" и попробовать снова.'})

        for i in edges:
            if len(i) != 2:
                return render(request, self.template_name_error)
            if len(i[0]) == 0 or len(i[1]) == 0:
                return render(request, self.template_name_error)
            i.append(i[0]+'->'+i[1]) #по индексу 2 строка для ребра диграфа
            i.append('')#по индексу 3 строка для стиля ребра диграфа
            i.append(True)#по индексу 4 узнаём пройдено ли ребро


        d = dict()
        for i in edges:
            if not i[0] in d.keys():
                d[i[0]] = 1
            else:
                d[i[0]] += 1
            if not i[1] in d.keys():
                d[i[1]] = -1
            else:
                d[i[1]] -= 1

        for i in d.values():
            if i != 0:
                return render(request, self.template_name_error,
                              context={'msg': 'Граф не является эйлеровым'})

        g = make_digraph(edges)
        data = []
        it = 1
        v_len = len(d.values())
        deal = len(edges) + 1
        v = edges[0][0]
        ans = [[v]]
        j = 0
        cycles = 0

        while it != deal:
            OK_edges = []
            for i in edges:
                if i[4]:
                    i[3] = ''
                else:
                    i[3] = '[color=grey]'

            while len(OK_edges) == 0:
                for i in range(0, len(edges)):
                    if edges[i][0] == v and edges[i][4]:
                        OK_edges.append([i, True])
                if len(OK_edges) == 0:
                    for i in range(0, len(edges)):
                        if edges[i][4]:
                            v = edges[i][0]
                            ans[j][0] = str(v)
                            break
                        if i == len(edges) - 1 and not edges[i][4]:
                            break

            not_find_true = True

            for i in OK_edges:
                if not i[1]:
                    edges[i[0]][3] = '[color=red,penwidth=5.0]'
                elif not_find_true:
                    not_find_true = False
                    edges[i[0]][3] = '[color=green,penwidth=5.0]'
                    edges[i[0]][4] = False
                    v = edges[i[0]][1]
                    ans[j].append(str(v))
                    if str(v) == ans[j][0]:
                        j += 1
                        ans.append([str(v)])
                else:
                    edges[i[0]][3] = '[color=yellow,penwidth=5.0]'
            data.append([it + cycles, make_digraph(edges)])
            if len(ans[j]) == 1:
                for i in edges:
                    if i[4]:
                        i[3] = ''
                    else:
                        i[3] = '[color=grey]'
                for r in range(len(ans[j - 1]) - 1):
                    for i in edges:
                        if i[0] == ans[j - 1][r] and i[1] == ans[j - 1][r + 1]:
                            i[3] = '[color=blue,penwidth=5.0]'
                cycles += 1
                data.append([it + cycles, make_digraph(edges)])
            it += 1

        count = len(data)

        ans2 = copy.deepcopy(ans)
        steps = 'В цикле 0: '
        answer = ''
        pos = 0
        cycle = 0
        stack = []

        for i in ans:
            i = i[0:len(ans) - 1]

        while True:
            flag = cycle
            for i in range(cycle + 1, len(ans)):
                for j in range(0, len(ans[i])):
                    if str(ans[i][j]) == str(ans[cycle][pos]):
                        stack.append([pos, cycle])
                        steps += '..' + str(ans[cycle][pos])
                        steps += '..перешли в цикл ' + str(i)
                        pos = j
                        cycle = i
                        last_down_cycle = False
                        break
            if flag == cycle:
                steps += '..' + str(ans[cycle][pos])
                if not last_down_cycle:
                    answer += '(' + str(ans[cycle][pos]) + ')'
                last_down_cycle = False
                ans[cycle][pos] = '>'
                pos += 1
                if pos == len(ans[cycle]):
                    pos = 0
                if ans[cycle][pos] == '>':
                    if len(stack) > 0:
                        pos = stack[len(stack) - 1][0]
                        cycle = stack[len(stack) - 1][1]
                        steps += '..вернулись в цикл ' + str(cycle)
                        stack = stack[0:len(stack) - 1]
                        last_down_cycle = True
                    else:
                        break
        # steps = 'В цикле 0: '
        # pos = 0
        # cycle = 0
        # stack = []
        #
        # while True:
        #     flag = cycle
        #     for i in range(cycle + 1, len(ans)):
        #         for j in range(0, len(ans[i])):
        #             if ans[i][j] == ans[cycle][pos]:
        #                 stack.append(pos)
        #                 cycle += 1
        #                 steps += '..перешли в цикл ' + str(cycle) + ' '
        #                 pos = j
        #                 break
        #     if flag == cycle:
        #         steps += '..' + str(ans[cycle][pos])
        #         answer += '(' + str(ans[cycle][pos]) + ')'
        #         ans[cycle][pos] = '>'
        #         pos += 1
        #         if pos == len(ans[cycle]) - 1:
        #             pos = 0
        #         if ans[cycle][pos] == '>':
        #             if len(stack) > 0:
        #                 pos = stack[len(stack) - 1]
        #                 cycle -= 1
        #                 steps += '..вернулись в цикл ' + str(cycle) + ' '
        #                 stack = stack[0:len(stack) - 1]
        #             else:
        #                 break

        args = {'data': data, 'count': count, 'ans': [ans2[0:len(ans2) - 1], answer], 'j': steps}

        return render(request, self.template_name_post, args)


def make_digraph(data):
    str = "digraph { rankdir=LR;"

    for i in data:
        str += i[2] + i[3] + ";"

    str += "}"
    return str

def make_digraph(data):
    str = "digraph { rankdir=LR;"

    for i in data:
        str += i[2] + i[3] + ";"

    str += "}"
    return str


def dfs_or_leave(edges, visited, fr, to):
    smth_chgd = True
    visited[fr] = True
    need_to_check = [fr]
    gg = False
    while (not gg) and smth_chgd:
        smth_chgd = False
        new = []
        for t in need_to_check:
            for i in edges:
                if t == i[0] and i[4] and (not visited[i[1]]):
                    if i[1] == to:
                        gg = True
                    smth_chgd = True
                    new.append(i[1])
                    visited[i[1]] = True
        need_to_check = new

    leave = False
    r = 0
    for i in edges:
        if (i[0] == to or to == i[1]) and i[4]:
            r += 1
    if r == 1:
        leave = True

    return gg or leave
