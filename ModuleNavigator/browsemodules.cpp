#include "browsemodules.h"
#include "./ui_browsemodules.h"

BrowseModules::BrowseModules(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::BrowseModules)
{
    ui->setupUi(this);
}

BrowseModules::~BrowseModules()
{
    delete ui;
}

