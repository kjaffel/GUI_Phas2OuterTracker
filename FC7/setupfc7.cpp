#include "setupfc7.h"
#include "ui_setupfc7.h"

setupFC7::setupFC7(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::setupFC7)
{
    ui->setupUi(this);
}

setupFC7::~setupFC7()
{
    delete ui;
}

