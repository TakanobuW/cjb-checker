<!-- <p align="center">
  <a href="https://gin-generate-random-name.df.r.appspot.com/" rel="noopener" target="_blank"><img width="90%" src="https://user-images.githubusercontent.com/31639255/107550423-5d931c80-6c14-11eb-90b8-2fdc5d301a02.png" alt="NameImpression logo"></a>
</p> -->


<h1 align="center">CJB-flie checker</h1>

<div align="center">

CJBファイルの動作確認やファイル内容の確認を行うためのツール

</div>

<h1>特徴</h1>

<h2>ファイル内容のチェック</h2>

選択したファイル群に対して, CJBファイルのパースを行い, ファイル情報の確認をすることができます.

<h2>動作の自動実行</h2>

選択したファイル群に対して自動実行を行い, 適切に動作するかをチェックすることができます.

<h2>豊富な出力</h2>

HTMLファイルとJSONファイルの2パターンで出力するため, 見やすい出力と, 扱いやすい出力を同時に得ることができます.

<h1>ダウンロードと実行</h1>

1. 本リポジトリのReleasesより, zipファイルをダウンロード
2. 解凍してプロジェクトディレクトリにて `main.py` を実行

<h1>Pythonの環境設定</h1>

本アプリはPython3.6以上での実行を想定しています.
また, インストールが必要なパッケージは `requirements.txt` にあるので, それを利用してインストールしてください.

<h1>各種設定について</h1>

<h2>選択方法の設定</h2>

対象ファイルの選択方法を選ぶことができます.

|      項目      |                               内容                               |
|:--------------:|:----------------------------------------------------------------:|
|  ファイル単位  |         確認対象となるファイルを1つ1つ選択していきます.          |
| フォルダー単位 | フォルダを指定して, その直下にある`.cjb`ファイルを全て取得します |

<h2>実行時の設定</h2>

自動実行時に関係する設定です. 基本的に秒数を長くするほど安定性が安定性が増し, 秒数を短くすると修了までにかかる時間が短くなります. よくわからない場合はデフォルト値で大丈夫です.

|              項目              |                         内容                         | デフォルト値 |
|:------------------------------:|:----------------------------------------------------:|:------------:|
|   各要素探索にかける時間(秒)   | seleniumにて, find_elementsする際の最大探索時間です. |     0.2      |
| 要素をクリック後の待機時間(秒) |       スイッチをクリックした後の待機時間です.        |     0.1      |

<h2>確認項目の設定</h2>

チェックを行う内容を選択することができます.

|        項目        |                         内容                         |
|:------------------:|:----------------------------------------------------:|
| ファイル内容の確認 |     ファイルデータをパースして, 内容を出力します     |
|   回路の動作確認   | 課題1か課題2の動作を自動で行い, その結果を出力します |

<h2>ブラウザパスの設定</h2>

利用するChromeブラウザの実行ファイルのパスを設定します. 何も選択しなかった場合はデフォルトのパスを取得します.
また, Windowsであれば プログラムフォルダ内の `%ProgramFIles%\Google\Chrome\Application` に大体あると思います.

ここで一々選択するのが手間だという方は, 予めchromeへのパスを通しておくと何も選択せずに実行することができます.

<h1>フォルダ/ファイルの選択</h1>

[あとで画像貼ります]

中央下にあるボタンを押すことで対象フォルダ/ファイルを追加することができます.
また, 余分に追加してしまった場合は表示されている対象をクリックすることで取り除くことができます.

<h1>ファイル内容の確認</h1>

実行ボタンをクリックすると, 各ファイルをパースしその結果が出力されます.
各カラムと内容については以下の表をご確認ください.

|    項目    |                                         内容                                          |
|:----------:|:-------------------------------------------------------------------------------------:|
|   fname    |                               拡張子を除いたファイル名                                |
|   bytes    |                                     ファイル容量                                      |
|    date    | ファイルの作成日時. ファイルオプションとは別にファイルデータとして埋め込んでいるもの. |
| device_num |                              利用されているデバイスの数                               |
|  x_centre  |                              デバイス群のx方向の重心位置                              |
|  y_centre  |                              デバイス群のy方向の重心位置                              |

出力された表は, ヘッダー部分をクリックするとその項目で昇順/降順に並び替えることができます.

<h1>回路の動作確認</h1>

実行ボタンをクリックすると, 動作の自動実行が行われます. Chromeが立ち上がり, アプリのプログレスバーが進み始めます.
大雑把ではありますが, 経過時間と予測残り時間も表示されます.

実行がすべて完了したら, その結果が表に出力されます. 各カラムと内容については以下の表をご確認ください.

|     項目      |                 内容                 |
|:-------------:|:------------------------------------:|
|     fname     |       拡張子を除いたファイル名       |
|  workability  |          正しく動作できたか          |
| error-details |      正しく実行できなかった原因      |
|    mapping    | 実行時の入力の状態と出力の状態の対応 |

出力された表は, ヘッダー部分をクリックするとその項目で昇順/降順に並び替えることができます.
また, 正しく実行できなかった場合, その行が赤くハイライトされます.

<h1>結果の出力</h1>

保存先のフォルダを選択し, 「結果を保存する」ボタンをクリックすると, そのフォルダに各種ファイルが保存されます.
各種結果の`htmlファイル`と`jsonファイル`が出力されます.

|     出力ファイル      |                 内容                 |
|:-------------:|:------------------------------------:|
|     file_result.html     |       ファイル内容をパースした結果が表記されたhtmlファイル       |
|     file_result.json     |       ファイル内容をパースした結果が格納JSONファイル       |
|     run_result.html     |       自動実行した結果が表記されたhtmlファイル       |
|     run_result.json     |       自動実行した結果が格納されたJSONファイル       |


<!-- <p><img src="https://raw.githubusercontent.com/gin-gonic/logo/master/color.png" alt="go-gin logo" width="25vw"> <a href="https://github.com/gin-gonic/gin" style="font-size: 5vw">Gin</a>: Gin is a web framework witten in Golang.</p> -->

<!-- <p><img src="https://user-images.githubusercontent.com/31639255/107553126-b7e1ac80-6c17-11eb-8cac-ec9e9d0c2db0.png" alt="React logo" width="35vw"> <a href="https://reactjs.org/" style="font-size: 5vw">React</a>: A JavaScript library for building user interfaces.</p> -->

<!-- <p><img src="https://user-images.githubusercontent.com/31639255/107553709-60900c00-6c18-11eb-884e-1b2d6f53117d.png" alt="App-Engine logo" width="33vw"> <a href="https://cloud.google.com/appengine/docs" style="font-size: 5vw">GAE</a>: GAE(Google App Engine) is a fully managed, serverless platform for developing and hosting web applications at scale.</p> -->
