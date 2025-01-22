from cob_eda.cli import group_by_count
import pandas as pd
import pytest


def test1():
    df=group_by_count("경제",False,5)
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]["president"] == "문재인"
    assert len(df) == 5

def test_search_exception():
    # 주어진변수
    row_count = 13
    df = group_by_count(keyword="자유", asorde=True, howmany=row_count)
    
    # assert
    assert isinstance(df, pd.DataFrame)
    assert len(df) < row_count

def test_정열_및_행수제한():
    # given
    row_count = 3
    is_asc = True

    # when
    df = group_by_count(keyword="자유", asorde=is_asc, howmany=row_count)
    
    # then
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]["president"] == "윤보선"
    assert len(df) == row_count

@pytest.mark.parametrize("asc,president",[(True,"윤보선"),(False,"박정희")])
def test_정열_및_행수제한(asc,president):
    # given
    rc = 3
    #asc = True

    # when
    df = group_by_count("자유",asorde=asc,howmany=rc)

    # then
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]["president"] == president
    #assert df.iloc[0]["count"]==1
    assert df.iloc[0]["president"] == president
    assert len(df) ==3
    #assert df.iloc[0]["count"]==513
    #assert df.iloc[1]["count"]==438

def test_딕셔너리확인():
    
    df = group_by_count("자유",False,12)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 12
    presidents_speeche = {}
    for i in range(len(df)):
        presidents_speeche[df.iloc[i]["president"]]=df.iloc[i]["count"]
    for i,v in presidents_speeche.items():
        assert presidents_speeche[i]==v
    
    assert presidents_speeche["박정희"]==513
    assert presidents_speeche["이승만"]==438
    assert presidents_speeche["윤보선"]==1


presidents_speeche = { "박정희": 513,"이승만": 438,"노태우": 399,"김대중": 305,"문재인": 275,"김영삼": 274,"이명박": 262,"전두환": 242,"노무현": 230,"박근혜": 111,"최규하": 14,"윤보선": 1 }


def test_all_count():
    #given
    #global presidents_speeche

    #when
    df = group_by_count("자유",False,12)

    #then
    assert isinstance(df,pd.DataFrame)
    assert len(df) == 12

    for p_name,s_count in presidents_speeche.items():
        president_row = df[df["president"] == p_name]
        assert president_row.iloc[0]["count"]== s_count
