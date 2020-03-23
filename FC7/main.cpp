#include "setupfc7.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    setupFC7 w;
    w.show();
    return a.exec();
}
