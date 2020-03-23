#include "daq_app.h"
#include "./ui_daq_app.h"
#include <QFile>
#include <QTextStream>

DAQ_APP::DAQ_APP(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::DAQ_APP)
{
    ui->setupUi(this);
}

DAQ_APP::~DAQ_APP()
{
    delete ui;
}
void TextFinder::loadTextFile()
{
    QFile inputFile(":/input.txt");
    inputFile.open(QIODevice::ReadOnly);

    QTextStream in(&inputFile);
    QString line = in.readAll();
    inputFile.close();

    ui->textEdit->setPlainText(line);
    QTextCursor cursor = ui->textEdit->textCursor();
    cursor.movePosition(QTextCursor::Start, QTextCursor::MoveAnchor, 1);
}

void TextFinder::on_findButton_clicked()
{
    QString searchString = ui->lineEdit->text();
    ui->textEdit->find(searchString, QTextDocument::FindWholeWords);
}

TextFinder::TextFinder(QWidget *parent)
    : QWidget(parent), ui(new Ui::TextFinder)
{
    ui->setupUi(this);
    loadTextFile();
}
