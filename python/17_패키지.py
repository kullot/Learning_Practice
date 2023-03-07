+++# 패키지
# 모듈을 디렉토리구조로 관리할수 있게 해준다

# 파이썬에서 모듈은 하나의 .py 파일이다

# Game
#   graphic
#       screen
#       render
#   sound
#       mp3
#       wav
#   play
#       walk++
#       run

import Game.sound.mp3.play as Sound # import뒤 as는 약자
# from Game.sound.mp3.play import play1
Sound.play1()
# Game.sound.mp3.play.play1()

