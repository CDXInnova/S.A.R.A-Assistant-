-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-07-2023 a las 21:48:34
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bitacora`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultoria`
--

CREATE TABLE `consultoria` (
  `numero` int(11) NOT NULL,
  `pregunta` varchar(500) NOT NULL,
  `respuesta_corta` mediumtext NOT NULL,
  `respuesta_detallada` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `consultoria`
--

INSERT INTO `consultoria` (`numero`, `pregunta`, `respuesta_corta`, `respuesta_detallada`) VALUES
(1, 'quién es tu creador', 'mi creador es cdx innova', ''),
(2, 'cómo alterar una tabla en mysql', 'usar alter table', 'usar alter table + la tabla + modificó lumen');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `consultoria`
--
ALTER TABLE `consultoria`
  ADD PRIMARY KEY (`numero`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `consultoria`
--
ALTER TABLE `consultoria`
  MODIFY `numero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
