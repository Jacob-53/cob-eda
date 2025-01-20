from president_speech.db.parquet_interpreter import read_parquet, get_parquet_full_path
import pandas as pd
import typer

app = typer.Typer()

@app.command()

def psearch_by_count(keyword: str ):
    data_path = get_parquet_full_path()
    df = pd.read_parquet(data_path)
    f_df = df[df['speech_text'].str.contains(str(keyword), case=False)]
    while True:
        if not f_df.empty:
            pass
        else:
            typer.echo(f" '{keyword}'은 언급 되지 않았습니다.")
            keyword = typer.prompt("새로운 키워드를 입력하세요")
    rdf = f_df.groupby("president").size().reset_index(name="count").sort_values(by="count", ascending=False)
    sdf = rdf.sort_values(by='count', ascending=False).reset_index(drop=True)
    print(sdf.to_string(index=False))

if __name__ == "__main__":
    app()


def group_by_count():
    kw = "올림픽"
    data_path = get_parquet_full_path()
    df = pd.read_parquet(data_path)
    f_df = df[df['speech_text'].str.contains(str(kw), case=False)]
    rdf = f_df.groupby("president").size().reset_index(name="count").sort_values(by="count", ascending=False)
    sdf = rdf.sort_values(by='count', ascending=False).reset_index(drop=True)
    print(sdf.to_string(index=False))
