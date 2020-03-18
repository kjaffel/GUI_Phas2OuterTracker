#include "ssmodule.h"
#include "ui_ssmodule.h"

SSModule::SSModule(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::SSModule)
{
    ui->setupUi(this);
}

SSModule::~SSModule()
{
    delete ui;
}

