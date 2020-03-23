#include "browsemodules.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    BrowseModules w;
    w.show();
    return a.exec();
}
