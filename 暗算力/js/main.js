// 変数定義
let randnumA = "";
let randnumB = "";
let questions = "";
let answers = "";
let inputValue = "";
let targetQ = "";
let targetA = "";
let quizCount = "";
let count = 0;
let score = 0;
let answerText = document.getElementById('answerText');
let timer = document.getElementById('timer');
let TIME = "";
let countDown = 0;
const startButton = document.getElementById('startButton');
let state = true;
let timerID = "";
let endFlg = "";
let courseText = "";
let digit = "";
let handler_focusin = "";
let handler_focusout = "";



// スタート画面表示
$('#pageStart').show();

$('#start_button').focus();

// スタートクリック関数
$('#startButton a').on('click',function(){

    $(this).blur();  
    $('#pageStart').hide();
    

    //courseText = document.getElementById('courseText');
    //course = courseText.value;
    course = document.getElementById('courseText').value;

    console.log("コース番号は" + course);

    // コースによる変数切り替え
    switch (course){
        case '':
            window.alert('コースが入力されていません！');
            $('#pageStart').show();
            let state = true;
            return;
        case 'A':
            digit = 100;
            TIME = 30;
            quizCount = 5;
            break;
        case 'B':
            digit = 100;
            TIME = 20;
            quizCount = 5;
            break;
        case 'C':
            digit = 1000;
            TIME = 60;
            quizCount = 5;
            break;
        case 'D':
            digit = 1000;
            TIME = 40;
            quizCount = 5;
            break;
        case 'E':
            digit = 10000;
            TIME = 90;
            quizCount = 5;
            break;
        case 'F':
            digit = 10000;
            TIME = 60;
            quizCount = 5;
            break;
        case 'G':
            digit = 100;
            TIME = 60;
            quizCount = 1000;
            break;
        case 'H':
            digit = 1000;
            TIME = 60;
            quizCount = 1000;
            break;
        case 'I':
            digit = 10000;
            TIME = 60;
            quizCount = 1000;
            break;
        default:
            window.alert('コース番号が不正です！');
            $('#pagePlaying').hide();
            $('#pageStart').show();
            state = true;
            return;
    }

    // プレイ画面表示
    $('#pageStart').hide();
    $('#pagePlaying').show();

    // カウントダウン関数
    $(function(){

        timerID = setInterval(function() {
            timer.textContent = '制限時間：' + --TIME + '秒';
            if(TIME <= 0) finish();
        }, 1000);

        // 制限時間超え関数
        function finish() {
            clearInterval(timerID);

            if (endFlg == 1) {

                state = false;
                return;
            
            } else {
                // 終了
                console.log("全問終了");
                window.alert("終了！");
                state = false;
                //return;
                $('#pagePlaying').hide();
                $('#pageEnd').show();

                // 結果発表関数を実行
                quizRusut();
                
            }
        }

        if(!state) return;        

        // 出題関数を実行（1回目）
        setupQuiz();

    });
});

// 出題関数
function setupQuiz () {

    if(!state) return;
  
    answerText.value = "";
    inputValue = "";

    console.log((count + 1) + "門目開始");
    
    targetQ = "";
    targetA = "";

    // 問題と回答を作成
    randnumA = Math.floor( Math.random() * digit );
    randnumB = Math.floor( Math.random() * digit );
    questions = randnumA + ' + ' + randnumB + ' =';
    answers = randnumA + randnumB;
    
    targetQ = questions;
    targetA = answers;

    // 問題画面を表示
    document.getElementById('number').textContent = "第" + (count + 1) + "門";
    document.getElementById('question').textContent = targetQ;
   
    // 回答欄へフォーカス
    answerText.focus();

    handler_focusout = () => {
        console.log("第" + (count + 1) + "門はフォーカスされていません。(addEventListener)");
        answerText.focus();
    }

    handler_focusin = () => {
        console.log("第" + (count + 1) + "門はフォーカスされました。(addEventListener)");
        answerText.removeEventListener("focusout", handler_focusout);
        console.log("第" + (count + 1) + "門のfoucusoutイベントは削除されました。(removeEventListener)");
    }

    answerText.addEventListener("focusout", handler_focusout); 
    answerText.addEventListener("focusin", handler_focusin);
      
}

// 入力回答チェック関数
function AnswerCheck () {

    if(!state) return;

    if (count < quizCount) {

        inputValue = answerText.value;

        // 正誤判定
        if (targetA == inputValue) {
            window.alert("正解！");
            score++;
        } else {
            window.alert("不正解！ 正解は " + targetA);
        }

        console.log((count + 1) + "門目終了");

        count++;

        if (count !== quizCount) {

            // 出題関数を実行（2回目以降）
            setupQuiz();

        } else {
            // 終了
            //window.alert('あなたの正解数は' + score + '/' + quizCount + 'です！');
            console.log("全問終了");
            window.alert("終了！");
            endFlg = 1;
            state = false;            
            //return;

            console.log("タイマーIDは" + timerID);
            console.log("タイマーは" + TIME);

            $('#pagePlaying').hide();
            $('#pageEnd').show();

            clearInterval(timerID);

            // 結果発表関数を実行
            quizRusut();

        }
    }
}

//結果発表関数
function quizRusut () {

    clearInterval(timerID);

    $('#back_button').focus();

    // 結果発表
    switch (course){
        case 'A':
        case 'B':
        case 'C':
        case 'D':
        case 'E':
        case 'F':    
            // 正解数を表示
            resultText.value = score + ' / ' + quizCount;
            console.log(score + ' / ' + quizCount);

            // 評価を表示    
            switch (score){
                case 5:
                    gradeText.value = '大変よくできました！！！';
                    break;
                case 4:
                case 3:
                    gradeText.value = 'よくできました！';
                    break;
                case 2:
                case 1:
                case 0:
                    gradeText.value = 'もっと頑張りましょう！';
                    break;
            }
            break;

        case 'G':
            // 正解数を表示
            resultText.value = score;
            console.log(score);
            
            // 評価を表示    
            switch (true){
                case score >= 20:
                    gradeText.value = '超優秀！！！';
                    break;
                case score >= 15:
                    gradeText.value = '優秀！';
                    break;
                case score >= 10:
                    gradeText.value = 'あと少し！';
                    break;
                case score < 10:
                    gradeText.value = '頑張れ！';
                    break;
            }
            break;

        case 'H':
            // 正解数を表示
            resultText.value = score;
            console.log(score);
            
            // 評価を表示    
            switch (true){
                case score >= 12:
                    gradeText.value = '超優秀！！！';
                    break;
                case score >= 8:
                    gradeText.value = '優秀！';
                    break;
                case score >= 5:
                    gradeText.value = 'あと少し！';
                    break;
                case score < 5:
                    gradeText.value = '頑張れ！';
                    break;    
            }
            break;

        case 'I':
            // 正解数を表示
            resultText.value = score;
            console.log(score);
            
            // 評価を表示    
            switch (true){
                case score >= 8:
                    gradeText.value = '超優秀！！！';
                    break;
                case score >= 5:
                    gradeText.value = '優秀！';
                    break;
                case score >= 2:
                    gradeText.value = 'あと少し！';
                    break;
                case score < 2:
                    gradeText.value = '頑張れ！';
                    break;    
            }
            break;
}

    // スタートに戻る
    $('#backStart a').on('click',function(){
        //$(this).blur();

        //$('#pageEnd').hide();
        //$('#pagePlaying').show();          
      
        location.reload();   
        
    });
};