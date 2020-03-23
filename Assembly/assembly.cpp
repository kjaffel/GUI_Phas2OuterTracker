#include "assembly.h"
#include "./ui_assembly.h"

Assembly::Assembly(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Assembly)
{
    ui->setupUi(this);
}

Assembly::~Assembly()
{
    delete ui;
}

