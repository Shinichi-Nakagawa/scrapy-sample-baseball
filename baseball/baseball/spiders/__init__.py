# 打撃・投球で共通して使う定義
LEAGUE_TOP = 1  # 一軍
LEAGUE_MINOR = 2  # 二軍

THROW_RIGHT = 'R'   # 右投げ
THROW_LEFT = 'L'    # 左投げ

BAT_RIGHT = 'R'   # 右打ち
BAT_LEFT = 'L'    # 左打ち
BAT_SWITCH = 'T'    # 両打ち

TEAMS = {
    'f': 'fighters',
    'h': 'hawks',
    'm': 'marines',
    'l': 'lions',
    'e': 'eagles',
    'bs': 'buffalos',
    'c': 'carp',
    'g': 'giants',
    'db': 'baystars',
    's': 'swallows',
    't': 'tigers',
    'd': 'dragons',
}


class BaseballSpidersUtil:

    @classmethod
    def get_team(cls, url):
        try:
            return TEAMS.get(url.replace('.html', '').split('_')[-1], 'Unknown')
        except IndexError:
            return 'Unknown'

    @classmethod
    def get_text(cls, text):
        """
        テキスト取得(ゴミは取り除く)
        :param text: text
        :return: str
        """
        if not text:
            return ''
        return text.replace('\u3000', ' ')

    @classmethod
    def text2digit(cls, text, digit_type=int):
        """
        数値にキャストする(例外時はゼロを返す)
        :param text: text
        :param digit_type: digit type(default:int)
        :return: str
        """
        if not text:
            return digit_type(0)
        try:
            return digit_type(text)
        except ValueError as e:
            print("変換に失敗しているよ:{}".format(e))
            return digit_type(0)