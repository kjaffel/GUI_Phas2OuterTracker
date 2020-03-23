#include "daq_app.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    DAQ_APP w;
    w.show();
    return a.exec();
}
