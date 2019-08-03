void MainWindow::tileSubWindowsHorizontally()
{

    if (mdiArea->subWindowList().isEmpty())
        return;

    QPoint position(0, 0);

    foreach (QMdiSubWindow * window, mdiArea->subWindowList()) {
        QRect rect(0, 0, mdiArea->width() / mdiArea->subWindowList().count(), mdiArea->height());
        window->setGeometry(rect);
        window->move(position);
        position.setX(position.x() + window->width());
    }
}