#include "modulesnavigator.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    ModulesNavigator w;
    w.show();
    return a.exec();
}
