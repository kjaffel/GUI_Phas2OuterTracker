#include "modulesnavigator.h"
#include "ui_modulesnavigator.h"

ModulesNavigator::ModulesNavigator(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::ModulesNavigator)
{
    ui->setupUi(this);
}

ModulesNavigator::~ModulesNavigator()
{
    delete ui;
}

