#ifndef BROWSEMODULES_H
#define BROWSEMODULES_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class BrowseModules; }
QT_END_NAMESPACE

class BrowseModules : public QMainWindow
{
    Q_OBJECT

public:
    BrowseModules(QWidget *parent = nullptr);
    ~BrowseModules();

private:
    Ui::BrowseModules *ui;
};
#endif // BROWSEMODULES_H
