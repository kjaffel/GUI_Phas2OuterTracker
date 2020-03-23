#include "assembly.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Assembly w;
    w.show();
    return a.exec();
}
