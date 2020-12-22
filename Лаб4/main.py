# ИССЛЕДОВАНИЕ И ОЦЕНКА АЛГОРИТМОВ ПОИСКА
# Цель работы:
#     Разработка программ, реализующих различные
#     алгоритмы поиска, и оценка их временной и пространственной сложности.
import time as t
import random
import plotly.express as px
import re


def accelerated_search(searchable: str, term: str, n):

    units = re.split('[\W\s]+', searchable)
    sortedunits = sorted(units)
    num = -1
    i = 0
    while i < n:
        if sortedunits[i] == term:
            num = i
        i += 1
    return num


def build_chart(raw):
    chart_data = []

    for (nn, time) in raw:
        chart_data.append(
            dict(
                size=nn,
                evaluation=time
            )
        )
    fig = px.line(chart_data, x="size", y="evaluation")
    fig.show()


sus = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean at feugiat odio, ut luctus ipsum. Mauris blandit sagittis purus, nec dignissim mauris lacinia vitae. Proin imperdiet aliquam erat nec cursus. Sed volutpat, neque et vehicula convallis, metus eros sollicitudin turpis, sit amet tristique elit est luctus massa. Nunc consectetur sed ligula eget faucibus. Etiam hendrerit dui ut lobortis auctor. Donec ornare ac nulla et sollicitudin. Aliquam sollicitudin dolor ut magna aliquam pellentesque eu ac lacus. Mauris auctor, urna ac gravida viverra, odio eros euismod purus, in hendrerit elit odio id lacus. Proin hendrerit vestibulum faucibus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean nec placerat libero. Donec nunc est, porta nec massa ac, pretium consectetur quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla non sodales diam, et congue lorem. Aenean at feugiat odio, ut luctus ipsum. Mauris blandit sagittis purus, nec dignissim mauris lacinia vitae. Proin imperdiet aliquam erat nec cursus. Sed volutpat, neque et vehicula convallis, metus eros sollicitudin turpis, sit amet tristique elit est luctus massa. Nunc consectetur sed ligula eget faucibus. Etiam hendrerit dui ut lobortis auctor. Donec ornare ac nulla et sollicitudin. Aliquam sollicitudin dolor ut magna aliquam pellentesque eu ac lacus. Mauris auctor, urna ac gravida viverra, odio eros euismod purus, in hendrerit elit odio id lacus. Proin hendrerit vestibulum faucibus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean nec placerat libero. Donec nunc est, porta nec massa ac, pretium consectetur quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla non sodales diam, et congue lorem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean molestie metus vel nisl faucibus efficitur. Proin porta porttitor risus, non vulputate nunc. Phasellus odio mauris, pharetra a neque a, varius eleifend nulla. Etiam dignissim in purus a commodo. Pellentesque odio nibh, condimentum ac blandit in, eleifend vel ipsum. Duis vulputate, leo ac pretium consequat, purus nisl hendrerit nisl, nec egestas ante nunc nec dolor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum tincidunt pellentesque facilisis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed quis porttitor massa. Phasellus eleifend ex placerat sagittis dapibus. Praesent est neque, placerat rhoncus facilisis a, ultrices molestie diam. Proin vestibulum lorem vehicula egestas condimentum. Ut volutpat, orci id dictum sollicitudin, ligula metus pulvinar erat, at cursus lectus magna ac felis.Sed non dui efficitur, finibus justo vitae, vestibulum erat. Morbi at nisl sagittis, posuere lacus ac, sagittis ex. Donec ac vulputate diam, eu viverra lorem. Nulla id justo ultricies, semper lorem et, pulvinar lorem. Duis dignissim vel dui elementum semper. Nulla varius, massa tincidunt hendrerit tristique, metus dolor vehicula lectus, ut finibus mauris tortor ut turpis. Nullam commodo vel nunc ut aliquet. Sed euismod erat leo, vel cursus lorem consectetur ac. Cras ac nulla mauris. Duis quis orci et nibh porttitor feugiat eu nec diam. Fusce non pulvinar tellus. Cras faucibus felis risus, at commodo turpis eleifend sed. Nunc pulvinar ante ut nisl accumsan molestie. Nulla blandit nisl est.Sed non dui efficitur, finibus justo vitae, vestibulum erat. Morbi at nisl sagittis, posuere lacus ac, sagittis ex. Donec ac vulputate diam, eu viverra lorem. Nulla id justo ultricies, semper lorem et, pulvinar lorem. Duis dignissim vel dui elementum semper. Nulla varius, massa tincidunt hendrerit tristique, metus dolor vehicula lectus, ut finibus mauris tortor ut turpis. Nullam commodo vel nunc ut aliquet. Sed euismod erat leo, vel cursus lorem consectetur ac. Cras ac nulla mauris. Duis quis orci et nibh porttitor feugiat eu nec diam. Fusce non pulvinar tellus. Cras faucibus felis risus, at commodo turpis eleifend sed. Nunc pulvinar ante ut nisl accumsan molestie. Nulla blandit nisl est. Suspendisse non velit vitae nunc gravida volutpat vel ac arcu.Sed non dui efficitur, finibus justo vitae, vestibulum erat. Morbi at nisl sagittis, posuere lacus ac, sagittis ex. Donec ac vulputate diam, eu viverra lorem. Nulla id justo ultricies, semper lorem et, pulvinar lorem. Duis dignissim vel dui elementum semper. Nulla varius, massa tincidunt hendrerit tristique, metus dolor vehicula lectus, ut finibus mauris tortor ut turpis. Nullam commodo vel nunc ut aliquet. Sed euismod erat leo, vel cursus lorem consectetur ac. Cras ac nulla mauris. Duis quis orci et nibh porttitor feugiat eu nec diam. Fusce non pulvinar tellus. Cras faucibus felis risus, at commodo turpis eleifend sed. Nunc pulvinar ante ut nisl accumsan molestie. Nulla blandit nisl est. Suspendisse non velit vitae nunc gravida volutpat vel ac arcu.Sed non dui efficitur, finibus justo vitae, vestibulum erat. Morbi at nisl sagittis, posuere lacus ac, sagittis ex. Donec ac vulputate diam, eu viverra lorem. Nulla id justo ultricies, semper lorem et, pulvinar lorem. Duis dignissim vel dui elementum semper. Nulla varius, massa tincidunt hendrerit tristique, metus dolor vehicula lectus, ut finibus mauris tortor ut turpis. Nullam commodo vel nunc ut aliquet. Sed euismod erat leo, vel cursus lorem consectetur ac. Cras ac nulla mauris. Duis quis orci et nibh porttitor feugiat eu nec diam. Fusce non pulvinar tellus. Cras faucibus felis risus, at commodo turpis eleifend sed. Nunc pulvinar ante ut nisl accumsan molestie. Nulla blandit nisl est. Suspendisse non velit vitae nunc gravida volutpat vel ac arcu.Sed non dui efficitur, finibus justo vitae, vestibulum erat. Morbi at nisl sagittis, posuere lacus ac, sagittis ex. Donec ac vulputate diam, eu viverra lorem. Nulla id justo ultricies, semper lorem et, pulvinar lorem. Duis dignissim vel dui elementum semper. Nulla varius, massa tincidunt hendrerit tristique, metus dolor vehicula lectus, ut finibus mauris tortor ut turpis. Nullam commodo vel nunc ut aliquet. Sed euismod erat leo, vel cursus lorem consectetur ac. Cras ac nulla mauris. Duis quis orci et nibh porttitor feugiat eu nec diam. Fusce non pulvinar tellus. Cras faucibus felis risus, at commodo turpis eleifend sed. Nunc pulvinar ante ut nisl accumsan molestie. Nulla blandit nisl est.Aenean at feugiat odio, ut luctus ipsum. Mauris blandit sagittis purus, nec dignissim mauris lacinia vitae. Proin imperdiet aliquam erat nec cursus. Sed volutpat, neque et vehicula convallis, metus eros sollicitudin turpis, sit amet tristique elit est luctus massa. Nunc consectetur sed ligula eget faucibus. Etiam hendrerit dui ut lobortis auctor. Donec ornare ac nulla et sollicitudin. Aliquam sollicitudin dolor ut magna aliquam pellentesque eu ac lacus. Mauris auctor, urna ac gravida viverra, odio eros euismod purus, in hendrerit elit odio id lacus. Proin hendrerit vestibulum faucibus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean nec placerat libero. Donec nunc est, porta nec massa ac, pretium consectetur quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean at feugiat odio, ut luctus ipsum. Mauris blandit sagittis purus, nec dignissim mauris lacinia vitae. Proin imperdiet aliquam erat nec cursus. Sed volutpat, neque et vehicula convallis, metus eros sollicitudin turpis, sit amet tristique elit est luctus massa. Nunc consectetur sed ligula eget faucibus. Etiam hendrerit dui ut lobortis auctor. Donec ornare ac nulla et sollicitudin. Aliquam sollicitudin dolor ut magna aliquam pellentesque eu ac lacus. Mauris auctor, urna ac gravida viverra, odio eros euismod purus, in hendrerit elit odio id lacus. Proin hendrerit vestibulum faucibus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean nec placerat libero. Donec nunc est, porta nec massa ac, pretium consectetur quam. Lorem ipsum dolor sit amet, Aenean at feugiat odio, ut luctus ipsum. Mauris blandit sagittis purus, nec dignissim mauris lacinia vitae. Proin imperdiet aliquam erat nec cursus. Sed volutpat, neque et vehicula convallis, metus eros sollicitudin turpis, sit amet tristique elit est luctus massa. Nunc consectetur sed ligula eget faucibus. Etiam hendrerit dui ut lobortis auctor. Donec ornare ac nulla et sollicitudin. Aliquam sollicitudin dolor ut magna aliquam pellentesque eu ac lacus. Mauris auctor, urna ac gravida viverra, odio eros euismod purus, in hendrerit elit odio id lacus. Proin hendrerit vestibulum faucibus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean nec placerat libero. Donec nunc est, porta nec massa ac, pretium consectetur quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla non sodales diam, et congue lorem. consectetur adipiscing elit. Nulla non sodales diam, et congue lorem. Nulla non sodales diam, et congue lorem. Suspendisse non velit vitae nunc gravida volutpat vel ac arcu. Praesent hendrerit id ex ac pretium. Praesent hendrerit id ex ac pretium. Praesent hendrerit id ex ac pretium. Praesent hendrerit id ex ac pretium. Suspendisse non velit vitae nunc gravida volutpat vel ac arcu. Praesent hendrerit id ex ac pretium. Pellentesque iaculis massa rhoncus diam blandit, vitae pharetra nibh dignissim. Nullam nec pretium erat. Aenean at feugiat odio, ut luctus ipsum.Suspendisse et tristique risus, a tempor nisi. Aenean a gravida magna, et tristique nulla. Morbi at magna rutrum, eleifend arcu vel, facilisis augue. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum non dolor nec magna mollis rutrum a id diam. Aenean mattis tincidunt nulla sit amet porta. Nam non purus auctor, mattis elit congue, ullamcorper magna. Nam at sem eros. Sed rhoncus ornare dictum. Nam dignissim rutrum elit, eget ornare enim accumsan id. Mauris blandit sagittis purus, nec dignissim mauris lacinia vitae. Proin imperdiet aliquam erat nec cursus. Sed volutpat, neque et vehicula convallis, metus eros sollicitudin turpis, sit amet tristique elit est luctus massa. Nunc consectetur sed ligula eget faucibus. Etiam hendrerit dui ut lobortis auctor. Donec ornare ac nulla et sollicitudin. Aliquam sollicitudin dolor ut magna aliquam pellentesque eu ac lacus. Mauris auctor, urna ac gravida viverra, odio eros euismod purus, in hendrerit elit odio id lacus. Proin hendrerit vestibulum faucibus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.Sed non dui efficitur, finibus justo vitae, vestibulum erat. Morbi at nisl sagittis, posuere lacus ac, sagittis ex. Donec ac vulputate diam, eu viverra lorem. Nulla id justo ultricies, semper lorem et, pulvinar lorem. Duis dignissim vel dui elementum semper.Aliquam semper sed diam tristique dignissim. Duis nec nunc rhoncus, faucibus ex quis, accumsan odio. Duis blandit quam vel quam iaculis ullamcorper sed sit amet leo. Sed ullamcorper nibh venenatis lectus porta lacinia. Etiam facilisis pellentesque magna, vel sagittis lacus dictum at. Praesent facilisis finibus ex, id tempus odio luctus in. Nullam fermentum nec arcu pellentesque porta. Phasellus vitae ligula sapien. Nulla euismod a metus id tempor. Aliquam euismod tincidunt pretium. Maecenas pretium augue at suscipit condimentum. In ac sapien imperdiet, mollis massa at, pellentesque libero. Nulla varius, massa tincidunt hendrerit tristique, metus dolor vehicula lectus, ut finibus mauris tortor ut turpis. Nullam commodo vel nunc ut aliquet. Sed euismod erat leo, vel cursus lorem consectetur ac. Cras ac nulla mauris. Duis quis orci et nibh porttitor feugiat eu nec diam. Fusce non pulvinar tellus. Cras faucibus felis risus, at commodo turpis eleifend sed. Nunc pulvinar ante ut nisl accumsan molestie. Nulla blandit nisl est. Suspendisse non velit vitae nunc gravida volutpat vel ac arcu. Praesent hendrerit id ex ac pretium. Aenean nec placerat libero. Donec nunc est, porta nec massa ac, pretium consectetur quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla non sodales diam, et congue lorem. Aenean molestie metus vel nisl faucibus efficitur. Proin porta porttitor risus, non vulputate nunc. Phasellus odio mauris, pharetra a neque a, varius eleifend nulla. Etiam dignissim in purus a commodo. Pellentesque odio nibh, condimentum ac blandit in, eleifend vel ipsum. Duis vulputate, leo ac pretium consequat, purus nisl hendrerit nisl, nec egestas ante nunc nec dolor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum tincidunt pellentesque facilisis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed quis porttitor massa. Phasellus eleifend ex placerat sagittis dapibus. Praesent est neque, placerat rhoncus facilisis a, ultrices molestie diam. Proin vestibulum lorem vehicula egestas condimentum. Ut volutpat, orci id dictum sollicitudin, ligula metus pulvinar erat, at cursus lectus magna ac felis. Pellentesque iaculis massa rhoncus diam blandit, vitae pharetra nibh dignissim. Nullam nec pretium erat."
units = re.split('[\W\s]+', sus)
sortedunits = sorted(units)
arg = input()


def evaluate_results(repetitions: int) -> list:
    meta = []
    for m in range(repetitions):
        n = random.randint(10, len(sortedunits))
        start_time1 = t.time()
        m = accelerated_search(sus, arg, n)
        finish_time1 = t.time()
        meta.append((n, finish_time1 - start_time1))
    return meta


build_chart(sorted(evaluate_results(20), key=lambda x: x[0]))


